import asyncio
from zingmp3 import ZingMp3Async

async def main():
    zi = ZingMp3Async()
    await zi.getDetailPlaylist("67ZFO8DZ")
    await zi.getDetailArtist("đen vâu")
    await zi.getSongInfo("ZWAF6UFD")
    await zi.getSongStreaming("ZWAF6UFD")
    await zi.getHomePage()
    await zi.getChartHome()
    await zi.getWeekChart("ZWAF6UFD")
    await zi.getNewReleaseChart()
    await zi.getTop100()
    await zi.search("rick roll")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())