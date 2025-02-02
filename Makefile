# Makefile
.PHONY: test build-linux build-windows clean run

# Установка зависимостей
install:
	pip install -r requirements.txt

# Запуск тестов и генерация HTML-отчета
test:
	pytest --html=test_report.html
	@echo "Отчет сохранен в test_report.html"

# Сборка для Linux
build-linux:
	pyinstaller --onefile --name TradingViewAnalog \
	--add-data "app/static:app/static" \
	--add-data "app/templates:app/templates" \
	--distpath dist/linux \
	start.py
	@cp test_report.html dist/linux/

# Сборка для Windows
build-windows:
	pyinstaller --onefile --name TradingViewAnalog.exe \
	--add-data "app/static;app/static" \
	--add-data "app/templates;app/templates" \
	--distpath dist/windows \
	start.py
	@cp test_report.html dist/windows/

# Очистка артефактов
clean:
	rm -rf dist/ build/ *.spec __pycache__ app/__pycache__ .pytest_cache test_report.html

# Запуск приложения
run:
	python start.py