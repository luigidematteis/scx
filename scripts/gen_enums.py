#!/usr/bin/env python3

from pathlib import Path

warning = """
/*
 * WARNING: This file is autogenerated from scripts/gen_enums.py. If you would
 * like to access an enum that is currently missing, add it to the script
 * and run it from the root directory to update this file.
 */

"""

enums = [
            ("scx_public_consts", "SCX_OPS_NAME_LEN"),
            ("scx_public_consts", "SCX_SLICE_DFL"),
            ("scx_public_consts", "SCX_SLICE_INF"),

            ("scx_dsq_id_flags", "SCX_DSQ_FLAG_BUILTIN"),
            ("scx_dsq_id_flags", "SCX_DSQ_FLAG_LOCAL_ON"),
            ("scx_dsq_id_flags", "SCX_DSQ_INVALID"),
            ("scx_dsq_id_flags", "SCX_DSQ_GLOBAL"),
            ("scx_dsq_id_flags", "SCX_DSQ_LOCAL"),
            ("scx_dsq_id_flags", "SCX_DSQ_LOCAL_ON"),
            ("scx_dsq_id_flags", "SCX_DSQ_LOCAL_CPU_MASK"),

            ("scx_ent_flags", "SCX_TASK_QUEUED"),
            ("scx_ent_flags", "SCX_TASK_RESET_RUNNABLE_AT"),
            ("scx_ent_flags", "SCX_TASK_DEQD_FOR_SLEEP"),
            ("scx_ent_flags", "SCX_TASK_STATE_SHIFT"),
            ("scx_ent_flags", "SCX_TASK_STATE_BITS"),
            ("scx_ent_flags", "SCX_TASK_STATE_MASK"),
            ("scx_ent_flags", "SCX_TASK_CURSOR"),

            ("scx_task_state", "SCX_TASK_NONE"),
            ("scx_task_state", "SCX_TASK_INIT"),
            ("scx_task_state", "SCX_TASK_READY"),
            ("scx_task_state", "SCX_TASK_ENABLED"),
            ("scx_task_state", "SCX_TASK_NR_STATES"),

            ("scx_ent_dsq_flags", "SCX_TASK_DSQ_ON_PRIQ"),

            ("scx_kick_flags", "SCX_KICK_IDLE"),
            ("scx_kick_flags", "SCX_KICK_PREEMPT"),
            ("scx_kick_flags", "SCX_KICK_WAIT"),

            ("scx_enq_flags", "SCX_ENQ_WAKEUP"),
            ("scx_enq_flags", "SCX_ENQ_HEAD"),
            ("scx_enq_flags", "SCX_ENQ_PREEMPT"),
            ("scx_enq_flags", "SCX_ENQ_REENQ"),
            ("scx_enq_flags", "SCX_ENQ_LAST"),
            ("scx_enq_flags", "SCX_ENQ_CLEAR_OPSS"),
            ("scx_enq_flags", "SCX_ENQ_DSQ_PRIQ"),
]

def localvar(symbol):
    return "__" + symbol

def gen_enums_bpf_h():
    autogen = Path.cwd() / "scheds" / "include" / "scx" / "enums.autogen.bpf.h"
    with open(autogen, "w") as f:
        f.write(warning)
        for _, symbol in enums:
            f.write("const volatile u64 {} __weak;\n".format(localvar(symbol)))
            f.write("#define {} {}\n".format(symbol, localvar(symbol)))
            f.write("\n")


def gen_enums_h():
    autogen = Path.cwd() / "scheds" / "include" / "scx" / "enums.autogen.h"
    with open(autogen, "w") as f:
        f.write(warning)
        f.write("#define SCX_ENUM_INIT(skel) do { \\\n")
        for kind, symbol in enums:
            f.write("\tSCX_ENUM_SET(skel, {}, {}); \\\n".format(kind, symbol))
        f.write("} while (0)\n")

"""
    Helper script for autogenerating relocatable enum headers.
"""
if __name__ == "__main__":
    gen_enums_bpf_h()
    gen_enums_h()

