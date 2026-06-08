#!/usr/bin/env python3
"""解析 Codex CLI 本地 JSONL 会话日志，统计 Token 用量。"""

import json
import glob
import os
from datetime import datetime
from collections import defaultdict

SESSION_DIR = os.path.expanduser("~/.codex/sessions")


def parse_sessions():
    """扫描所有 JSONL 会话文件，提取 token_count 事件。"""
    pattern = os.path.join(SESSION_DIR, "**", "*.jsonl")
    files = glob.glob(pattern, recursive=True)
    files.sort()

    daily = defaultdict(lambda: {
        "input_tokens": 0,
        "cached_input_tokens": 0,
        "output_tokens": 0,
        "reasoning_output_tokens": 0,
        "total_tokens": 0,
        "sessions": set(),
    })
    session_summaries = []
    model_usage = defaultdict(lambda: {
        "input_tokens": 0,
        "cached_input_tokens": 0,
        "output_tokens": 0,
        "reasoning_output_tokens": 0,
        "total_tokens": 0,
        "count": 0,
    })

    total_sessions = 0

    for fpath in files:
        session_id = os.path.basename(fpath).replace(".jsonl", "")
        session_model = None
        session_tokens = {
            "input_tokens": 0,
            "cached_input_tokens": 0,
            "output_tokens": 0,
            "reasoning_output_tokens": 0,
            "total_tokens": 0,
        }
        session_date = None

        with open(fpath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue

                # 提取模型信息
                if record.get("type") == "turn_context":
                    payload = record.get("payload", {})
                    model = payload.get("model")
                    if model:
                        session_model = model

                # 提取 token 用量（只取 last_token_usage 避免重复累加）
                if record.get("type") == "event_msg":
                    payload = record.get("payload", {})
                    if payload.get("type") == "token_count":
                        info = payload.get("info", {})
                        last_usage = info.get("last_token_usage", {})
                        if last_usage:
                            ts = record.get("timestamp", "")
                            if ts:
                                try:
                                    dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                                    session_date = dt.strftime("%Y-%m-%d")
                                except ValueError:
                                    pass

                            session_tokens["input_tokens"] = last_usage.get("input_tokens", 0)
                            session_tokens["cached_input_tokens"] = last_usage.get("cached_input_tokens", 0)
                            session_tokens["output_tokens"] = last_usage.get("output_tokens", 0)
                            session_tokens["reasoning_output_tokens"] = last_usage.get("reasoning_output_tokens", 0)
                            session_tokens["total_tokens"] = last_usage.get("total_tokens", 0)

        if session_tokens["total_tokens"] > 0:
            total_sessions += 1

            # 按日汇总
            if session_date:
                d = daily[session_date]
                for key in ["input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens", "total_tokens"]:
                    d[key] += session_tokens[key]
                d["sessions"].add(session_id)

            # 按模型汇总
            model_name = session_model or "unknown"
            m = model_usage[model_name]
            for key in ["input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens", "total_tokens"]:
                m[key] += session_tokens[key]
            m["count"] += 1

            session_summaries.append({
                "date": session_date,
                "model": session_model,
                "session_id": session_id[-12:],
                **session_tokens,
            })

    return daily, model_usage, session_summaries, total_sessions


def fmt(n):
    """格式化数字，带千分位。"""
    if n >= 1_000_000:
        return f"{n / 1_000_000:,.2f}M"
    elif n >= 1_000:
        return f"{n / 1_000:,.1f}K"
    return str(n)


def main():
    daily, model_usage, sessions, total_sessions = parse_sessions()

    # 总量汇总
    grand = {
        "input_tokens": 0,
        "cached_input_tokens": 0,
        "output_tokens": 0,
        "reasoning_output_tokens": 0,
        "total_tokens": 0,
    }
    for d in daily.values():
        for key in grand:
            grand[key] += d[key]

    non_cached_input = grand["input_tokens"] - grand["cached_input_tokens"]
    net_usage = non_cached_input + grand["output_tokens"]
    cache_rate = (grand["cached_input_tokens"] / grand["input_tokens"] * 100) if grand["input_tokens"] > 0 else 0

    print("=" * 65)
    print("  Codex CLI Token 用量统计")
    print("=" * 65)
    print()

    # 总览
    print("【总览】")
    print(f"  会话总数:          {total_sessions}")
    print(f"  统计天数:          {len(daily)}")
    print(f"  总 Token:          {fmt(grand['total_tokens'])}")
    print(f"  输入 Token:        {fmt(grand['input_tokens'])} (含缓存)")
    print(f"  缓存命中 Token:    {fmt(grand['cached_input_tokens'])}")
    print(f"  非缓存输入:        {fmt(non_cached_input)}")
    print(f"  输出 Token:        {fmt(grand['output_tokens'])}")
    print(f"  推理输出 Token:    {fmt(grand['reasoning_output_tokens'])}")
    print(f"  净用量:            {fmt(net_usage)}  (非缓存输入 + 输出)")
    print(f"  缓存命中率:        {cache_rate:.2f}%")
    if daily:
        days = len(daily)
        print(f"  日均总量:          {fmt(grand['total_tokens'] // days)}")
    print()

    # 按日统计
    print("【按日统计】")
    print(f"  {'日期':<14} {'会话':>4} {'输入':>12} {'缓存':>12} {'输出':>12} {'总量':>12}")
    print("  " + "-" * 68)
    for date in sorted(daily.keys()):
        d = daily[date]
        print(f"  {date:<14} {len(d['sessions']):>4} {fmt(d['input_tokens']):>12} {fmt(d['cached_input_tokens']):>12} {fmt(d['output_tokens']):>12} {fmt(d['total_tokens']):>12}")
    print()

    # 按模型统计
    print("【按模型统计】")
    print(f"  {'模型':<22} {'调用次数':>6} {'输入':>12} {'输出':>12} {'总量':>12}")
    print("  " + "-" * 68)
    for model in sorted(model_usage.keys()):
        m = model_usage[model]
        print(f"  {model:<22} {m['count']:>6} {fmt(m['input_tokens']):>12} {fmt(m['output_tokens']):>12} {fmt(m['total_tokens']):>12}")
    print()

    # 最多的一天
    if daily:
        max_day = max(daily.keys(), key=lambda k: daily[k]["total_tokens"])
        d = daily[max_day]
        print(f"  最多的一天: {max_day} ({fmt(d['total_tokens'])} tokens, {len(d['sessions'])} 个会话)")
    print()


if __name__ == "__main__":
    main()
