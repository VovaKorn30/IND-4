import molotov
import asyncio

@molotov.scenario()
async def test_json(session):
    async with session.get("http://localhost:8000/test") as resp:
        assert resp.status == 200
        data = await resp.json()
        # Перевірка, що JSON має хоча б один ключ
        assert isinstance(data, dict)
        assert len(data) > 0
