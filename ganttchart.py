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

        #fix all of these
        {"Task": "Register (F1)",                                           "Start": "2025-11-03", "End": "2025-11-10"},
        {"Task": "Login (F2)",                                              "Start": "2025-11-10", "End": "2025-11-20"},
        {"Task": "Compare (F3)",                                            "Start": "2026-01-25", "End": "2026-01-30"},
        {"Task": "Search Box (F4)",                                         "Start": "2025-12-10", "End": "2025-12-25"},
        {"Task": "Product Cart (F5)",                                       "Start": "2025-12-15", "End": "2025-12-30"},
        {"Task": "Update Product Quantity  (F6)",                                       "Start": "2026-01-01", "End": "2026-01-10"},
        {"Task": "Swiper Controller buttons (F7)",                          "Start": "2026-01-9", "End": "2026-01-15"},
        {"Task": "Top collection category filter (F8)",                     "Start": "2026-01-15", "End": "2026-01-20"},
        {"Task": "Top collection Product Detail (F9)",                      "Start": "2026-01-18", "End": "2026-01-23"},
        {"Task": "Edit Account Information (F10)",                           "Start": "2025-11-20", "End": "2025-11-30"},
        {"Task": "Make a comment on blog (F11)",                            "Start": "2025-11-30", "End": "2025-12-15"},
        {"Task": "Filtering Product (F12)",                           "Start": "2026-01-15", "End": "2026-01-25"},
        {"Task": "Write a product review (F13)",                            "Start": "2025-12-25", "End": "2026-01-05"},
        {"Task": "Add address in address book (F14)",                       "Start": "2025-12-01", "End": "2025-12-15"},
        {"Task": "Purchase a Gift Certificate (F15)",                       "Start": "2026-01-20", "End": "2026-01-25"},
        {"Task": "Quick View Modal  (F16)",                    "Start": "2026-01-15", "End": "2026-01-20"},
        {"Task": "Add to Wish List (F17)",                    "Start": "2026-01-20", "End": "2026-01-25"},
        {"Task": "Product Comparison (F18)",                    "Start": "2025-11-10", "End": "2025-11-20"},
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
ax.set_title("Software Testing Gantt Chart")
plt.tight_layout()

#save pic as png
plt.savefig("gantt_chart.png", dpi=150, bbox_inches="tight")
plt.show()
