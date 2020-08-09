from aiohttp import web


def index(request):
    return web.Response(text = 'Hello, world!')


def health(request):
    return web.Response(text = 'OK')


app = web.Application()
app.add_routes([web.get('/', index), web.get('/actuator/health', health)])
