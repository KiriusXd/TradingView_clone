// app.js
async function loadData() {
    const symbol = document.getElementById('symbol').value;
    const timeframe = document.getElementById('timeframe').value;
    
    try {
        // Запрос данных с сервера
        const response = await fetch(`/api/ohlcv/${symbol}?timeframe=${timeframe}`);
        const data = await response.json();
        // Проверка статуса ответа
        if (!response.ok) {
            throw new Error(`Ошибка HTTP: ${response.status}`);
        }
        // Проверка, что данные являются массивом
        if (!Array.isArray(data)) {
            throw new Error("Данные не в формате массива");
        }
        // Подготовка данных для графика
        const dates = data.map(entry => new Date(entry[0]).toISOString());
        const open = data.map(entry => entry[1]);
        const high = data.map(entry => entry[2]);
        const low = data.map(entry => entry[3]);
        const close = data.map(entry => entry[4]);

        // Отрисовка графика
        const chartData = [{
            x: dates,
            close: close,
            high: high,
            low: low,
            open: open,
            type: 'candlestick',
            name: symbol
        }];

        const layout = {
            title: `${symbol} (${timeframe})`,
            xaxis: { type: 'date' },
            yaxis: { title: 'Price' },
            plot_bgcolor: '#222',
            paper_bgcolor: '#222',
            font: { color: '#fff' }
        };

        Plotly.newPlot('chart', chartData, layout);
    } catch (error) {
        alert('Ошибка загрузки данных: ' + error.message);
    }
    async function loadData() {
    const symbol = document.getElementById('symbol').value;
    const timeframe = document.getElementById('timeframe').value;
    
    try {
        const response = await fetch(`/api/ohlcv/${symbol}?timeframe=${timeframe}`);
        
        // Проверка статуса ответа
        if (!response.ok) {
            throw new Error(`Ошибка HTTP: ${response.status}`);
        }

        const data = await response.json();

        // Проверка, что данные являются массивом
        if (!Array.isArray(data)) {
            throw new Error("Данные не в формате массива");
        }

        // Отрисовка графика
        const dates = data.map(entry => new Date(entry[0]).toISOString());
        const open = data.map(entry => entry[1]);
        const high = data.map(entry => entry[2]);
        const low = data.map(entry => entry[3]);
        const close = data.map(entry => entry[4]);

        // ... остальной код отрисовки ...

    } catch (error) {
        alert('Ошибка загрузки данных: ' + error.message);
        console.error(error);
    }
}
}

// Загрузить данные при старте
window.onload = () => loadData();