.PHONY: fedev bedev beprod

fedev:
	cd fe && npm run dev
bedev:
	cd allaboutdjango && uv run manage.py runserver
beprod:
	cd allaboutdjango && uv run uvicorn allaboutdjango.asgi:application --workers 4