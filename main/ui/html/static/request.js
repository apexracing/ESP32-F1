// GET 请求函数
function get(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) { // 请求完成
            if (xhr.status >= 200 && xhr.status < 300) { // 请求成功
                var responseData = JSON.parse(xhr.responseText); // 假设返回的数据是 JSON 格式
                callback(null, responseData);
            } else {
                callback('Request failed with status ' + xhr.status);
            }
        }
    };

    xhr.onerror = function () {
        callback('请检查是否连接到设备的Wi-Fi热点');
    };

    xhr.send();
}

// POST 请求函数
function post(url, data, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) { // 请求完成
            if (xhr.status >= 200 && xhr.status < 300) { // 请求成功
                var responseData = JSON.parse(xhr.responseText); // 假设返回的数据是 JSON 格式
                callback(null, responseData);
            } else {
                callback('Request failed with status ' + xhr.status);
            }
        }
    };

    xhr.onerror = function () {
        callback('请检查是否连接到设备的Wi-Fi热点');
    };

    xhr.send(JSON.stringify(data)); // 将 JavaScript 对象转换为 JSON 字符串
}