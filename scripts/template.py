import datetime
import os
import json
from pathlib import Path
import argparse

# Constants
AUTHOR = "Anonymous"
TEMPLATE_PATH = Path("templates/")
TUTORIAL_DATES = [
    datetime.date(2025, 9, 18),
    datetime.date(2025, 9, 25),
    datetime.date(2025, 10, 2),
    datetime.date(2025, 10, 9),
    datetime.date(2025, 10, 23),
    datetime.date(2025, 10, 30),
    datetime.date(2025, 11, 6),
    datetime.date(2025, 11, 13),
    datetime.date(2025, 11, 20),
    datetime.date(2025, 11, 27),  # May not have a tutorial that week
]
SEPARATOR = "\n"


def load_tex(name: str) -> str:
    if os.path.exists(f"{TEMPLATE_PATH}/{name}.tex"):
        return Path(f"{TEMPLATE_PATH}/{name}.tex").read_text(encoding="utf-8").strip()

    misc = json.loads(Path(f"{TEMPLATE_PATH}/misc.json").read_text(encoding="utf-8"))
    if name in misc:
        return misc[name].strip()

    raise ValueError(f"Template '{name}' not found.")


def duplicate_braces(s: str) -> str:
    return s.replace("{", "{{").replace("}", "}}")


def fmt_date(date: datetime.date, year: bool = False) -> str:
    retval: str = f"{date.strftime('%B')} {date.day}"
    if year:
        retval += f", {date.year}"
    return retval


def get_head_frames() -> str:
    return load_tex("head").format().strip()


def get_recap_frames(count: int) -> str:
    frames: list[str] = []
    for index in range(1, count + 1):
        frame = load_tex("recp").format(title=f"TODO{index}RC")
        # frames.append(duplicate_braces(frame))
        frames.append(frame)
    return SEPARATOR.join(frames).strip()


def get_extension_frames(count: int) -> str:
    frames: list[str] = []
    for index in range(1, count + 1):
        frame = load_tex("extn").format(title=f"TODO{index}ET")
        # frames.append(duplicate_braces(frame))
        frames.append(frame)
    return SEPARATOR.join(frames).strip()


def get_practice_frame(count: int) -> str:
    items = "\n        ".join(
        load_tex("item").format(value=f"TODO{index}EX") for index in range(1, count + 1)
    )
    # items = duplicate_braces(items)
    return load_tex("prac").format(items=items).strip()


def get_mcq_frames(count: int) -> str:
    frames: list[str] = []
    for index in range(1, count + 1):
        frame = (load_tex("mcqq") + "\n" + load_tex("mcqs")).format(index=index)
        # frames.append(duplicate_braces(frame))
        frames.append(frame)
    return SEPARATOR.join(frames).strip()


def get_exercise_frames(
    count: int, sols: list[int] | None = None, alts: list[int] | None = None
) -> str:
    if sols is None:
        sols = [1] * count
    if alts is None:
        alts = [0] * count

    frames: list[str] = []
    for index, sol, alt in zip(range(1, count + 1), sols, alts):
        title = f"TODO{index}EX"
        frame = load_tex("exeq").format(title=title) + "\n"
        frame += (load_tex("exes").format(title=title) + "\n") * sol
        frame += (load_tex("exea").format(title=title) + "\n") * alt
        # frames.append(duplicate_braces(frame))
        frames.append(frame)
    return SEPARATOR.join(frames).strip()


def get_tail_frames(index: int) -> str:
    curr_date = TUTORIAL_DATES[index - 1]
    due_date = curr_date + datetime.timedelta(days=8)
    if index > 1:
        prev_date = TUTORIAL_DATES[index - 2] + datetime.timedelta(days=8)
        prev_reminder = (
            load_tex("srmd").format(
                index=index,
                date=fmt_date(prev_date),
            )
            if prev_date > curr_date
            else ""
        )
    else:
        prev_reminder = ""

    curr_reminder: str = load_tex("nrmd").format(
        index=index,
        date=fmt_date(due_date),
    )
    return (
        load_tex("tail")
        .format(curr_reminder=curr_reminder, prev_reminder=prev_reminder)
        .strip()
    )


def get_latex(
    index: int, author: str, recap: int, extension: int, mcq: int, exercise: int
) -> str:
    if index < 1 or index > len(TUTORIAL_DATES):
        raise ValueError(f"Index {index} is out of range.")

    head_frames = get_head_frames()
    recap_frames = get_recap_frames(recap)
    extension_frames = get_extension_frames(extension)
    practice_frame = get_practice_frame(exercise)
    mcq_frames = get_mcq_frames(mcq)
    exercise_frames = get_exercise_frames(exercise)
    tail_frames = get_tail_frames(index)

    template = load_tex("temp")
    return template.format(
        index=index,
        author=author,
        date=fmt_date(TUTORIAL_DATES[index - 1], year=True),
        head_frames=head_frames,
        recap_frames=recap_frames,
        extension_frames=extension_frames,
        practice_frame=practice_frame,
        mcq_frames=mcq_frames,
        exercise_frames=exercise_frames,
        tail_frames=tail_frames,
    )


def save_latex(content: str, out: Path, force: bool = False) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)

    if out.exists() and not force:
        raise FileExistsError(f"File '{out}' already exists. Use --force to overwrite.")
    out.write_text(content, encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser(
        description="生成 COMP1117 Tutorial Slides LaTeX 模板和相关文件结构"
    )
    parser.add_argument("index", type=int, default=1, help="Tutorial 编号")
    parser.add_argument(
        "--author",
        type=str,
        default=AUTHOR,
        help="作者姓名（默认: %(default)s）",
    )
    parser.add_argument(
        "-1",
        "--recap",
        type=int,
        default=2,
        help="Recap Frames 数量（默认: %(default)s）",
    )
    parser.add_argument(
        "-2",
        "--extension",
        type=int,
        default=2,
        help="Extension Frames 数量（默认: %(default)s）",
    )
    parser.add_argument(
        "-3",
        "--mcq",
        type=int,
        default=5,
        help="MCQ Frames 数量（默认: %(default)s）",
    )
    parser.add_argument(
        "-4",
        "--exercise",
        type=int,
        default=3,
        help="Exercise Frames 数量（默认: %(default)s）",
    )

    parser.add_argument(
        "--out",
        type=str,
        default=None,
        help="输出 tex 文件路径（默认创建Tutorial/src文件夹）",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="如果输出文件已存在则覆盖",
    )

    args = parser.parse_args()

    out: Path = (
        Path(args.out)
        if args.out
        else Path.cwd() / f"Tutorial{args.index}" / "src" / f"tut{args.index}.tex"
    )
    author: str = args.author
    index: int = args.index
    recap: int = args.recap
    extension: int = args.extension
    mcq: int = args.mcq
    exercise: int = args.exercise
    force: bool = args.force

    tex: str = get_latex(
        index=index,
        author=author,
        recap=recap,
        extension=extension,
        mcq=mcq,
        exercise=exercise,
    )
    print(f"已生成 LaTeX 文件: {save_latex(tex, out, force)}")


if __name__ == "__main__":
    main()
