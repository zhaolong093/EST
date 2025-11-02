# gantt.py
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 1) Load data ---------------------------------------------------------------
# CSV format: Task,Start,End  (dates like 2025-11-03)
csv_path = "gantt.csv"
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame([
        {"Task": "Register (F1)",                                           "Start": "2025-11-03", "End": "2025-11-14"},
        {"Task": "Login (F2)",                                              "Start": "2025-11-10", "End": "2025-11-25"},
        {"Task": "Compare (F3)",                                            "Start": "2025-11-17", "End": "2025-12-05"},
        {"Task": "Search Box (F4)",                                         "Start": "2025-12-05", "End": "2025-12-20"},
        {"Task": "Product Cart (F5)",                                       "Start": "2025-12-10", "End": "2026-01-08"},
        {"Task": "Swiper Controller buttons (F6)",                          "Start": "2026-01-01", "End": "2026-01-15"},
        {"Task": "Top collection category filter (F7)",                     "Start": "2026-01-15", "End": "2026-01-20"},
        {"Task": "Top collection Product Detail (F8)",                      "Start": "2026-01-18", "End": "2026-01-23"},
        {"Task": "Edit Account Information (F9)",                           "Start": "2026-01-20", "End": "2026-01-25"},
        {"Task": "Make a comment on blog (F10)",                            "Start": "2025-11-25", "End": "2025-12-10"},
        {"Task": "Filtering search result (F11)",                           "Start": "2026-01-05", "End": "2026-01-15"},
        {"Task": "Write a product review (F12)",                            "Start": "2025-12-10", "End": "2025-12-30"},
        {"Task": "Add address in address book (F13)",                       "Start": "2026-01-08", "End": "2026-01-12"},
        {"Task": "Purchase a Gift Certificate (F14)",                       "Start": "2026-01-20", "End": "2026-01-25"},
        {"Task": "Top collection category filter (F15)",                    "Start": "2026-01-15", "End": "2026-01-30"},
    ])

# 2) Prep data ---------------------------------------------------------------
df["Start"] = pd.to_datetime(df["Start"])
df["End"]   = pd.to_datetime(df["End"])
df = df.sort_values("Start").reset_index(drop=True)

# 3) Plot --------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5))

y = range(len(df))
dur = (df["End"] - df["Start"]).dt.days
ax.barh(list(y), dur, left=df["Start"].map(mdates.date2num))  # single plot, default colors

ax.set_yticks(list(y))
ax.set_yticklabels(df["Task"])
ax.invert_yaxis()  # tasks top->bottom

ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b %Y"))
fig.autofmt_xdate()

ax.set_xlabel("Timeline")
ax.set_title("Project Gantt Chart")
plt.tight_layout()

#save pic as png
plt.savefig("gantt_chart.png", dpi=150, bbox_inches="tight")
plt.show()
