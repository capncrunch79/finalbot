import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

import asyncio
from strategies.short_relief_rally import short_relief_rally_check
from strategies.short_breakdown_support import short_breakdown_support_check
from strategies.bear_flag_breakdown import bear_flag_breakdown_check
from strategies.head_shoulders_reversal import head_shoulders_reversal_check
from strategies.rising_wedge_short import rising_wedge_short_check
from strategies.ma_resistance_short import ma_resistance_short_check
from strategies.break_retest_short import break_retest_short_check
from strategies.resistance_zone_short import resistance_zone_short_check
from strategies.mean_reversion_volatility import mean_reversion_volatility_check
from strategies.event_driven_short import event_driven_short_check
from utils.notifier import notify_user

async def run_bot():
    while True:
        try:
            await short_relief_rally_check()
            await short_breakdown_support_check()
            await bear_flag_breakdown_check()
            await head_shoulders_reversal_check()
            await rising_wedge_short_check()
            await ma_resistance_short_check()
            await break_retest_short_check()
            await resistance_zone_short_check()
            await mean_reversion_volatility_check()
            await event_driven_short_check()
        except Exception as e:
            print("Error:", e)
            notify_user(f"Bot Error: {str(e)}")
        await asyncio.sleep(300)

if __name__ == "__main__":
    asyncio.run(run_bot())
