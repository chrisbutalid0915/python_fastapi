import fastapi

from models.location import Location
from models.umbrella_status import UmbrellaStatus
from services import get_live_weather
router = fastapi.APIRouter()


@router.get('/api/umbrella', response_model=UmbrellaStatus)
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()):
    data = await get_live_weather.get_live_report(location)

    weather = data.get('weather', {})
    category = weather.get('category', 'UNKNOWN')

    forecast = data.get('forecast', {})
    temp = forecast.get('temp', 0.0)

    bring = category.lower().strip() in {'rain', 'mist'}

    return UmbrellaStatus(bring_umbrella=bring, temp=temp, weather=category)


