(function () {
  "use strict";

  const DEFAULT_API_URL = "http://127.0.0.1:5000/api/v1";
  const elements = {
    form: document.getElementById("connection-form"),
    url: document.getElementById("api-url"),
    token: document.getElementById("api-token"),
    status: document.getElementById("connection-status"),
    connectButton: document.getElementById("connect-button"),
    endpoint: document.getElementById("endpoint"),
    queryButton: document.getElementById("query-button"),
    responseMeta: document.getElementById("response-meta"),
    responseHead: document.getElementById("response-head"),
    responseBody: document.getElementById("response-body")
  };
  let config = loadConfig();
  let connected = false;

  function loadConfig() {
    try {
      const saved = JSON.parse(localStorage.getItem("pc-gaming-api-config") || "{}");
      return {
        url: typeof saved.url === "string" && saved.url ? saved.url : DEFAULT_API_URL,
        token: typeof saved.token === "string" ? saved.token : ""
      };
    } catch (error) {
      console.error("No se pudo leer la configuración guardada.", error);
      return { url: DEFAULT_API_URL, token: "" };
    }
  }

  function setStatus(message, state) {
    elements.status.textContent = "Estado: " + message;
    elements.status.dataset.state = state;
  }

  function formatValue(value) {
    if (value === null || value === undefined) return "—";
    if (typeof value === "object") return JSON.stringify(value);
    return String(value);
  }

  function showMessage(message) {
    elements.responseHead.replaceChildren();
    elements.responseBody.replaceChildren();
    const row = document.createElement("tr");
    const cell = document.createElement("td");
    cell.className = "empty-state";
    cell.textContent = message;
    cell.colSpan = 1;
    row.appendChild(cell);
    elements.responseBody.appendChild(row);
  }

  function renderRows(data) {
    elements.responseHead.replaceChildren();
    elements.responseBody.replaceChildren();
    if (!Array.isArray(data) || data.length === 0) {
      showMessage(Array.isArray(data) ? "La consulta no devolvió registros." : "La respuesta no contiene una lista de registros.");
      return;
    }

    const columns = Array.from(new Set(data.reduce(function (keys, item) {
      if (item && typeof item === "object" && !Array.isArray(item)) {
        Object.keys(item).forEach(function (key) {
          if (!keys.includes(key)) keys.push(key);
        });
      }
      return keys;
    }, [])));
    if (columns.length === 0) {
      showMessage("La respuesta no contiene datos para mostrar.");
      return;
    }

    columns.forEach(function (column) {
      const heading = document.createElement("th");
      heading.scope = "col";
      heading.textContent = column;
      elements.responseHead.appendChild(heading);
    });

    data.forEach(function (item) {
      const row = document.createElement("tr");
      columns.forEach(function (column) {
        const cell = document.createElement("td");
        cell.textContent = formatValue(item && item[column]);
        row.appendChild(cell);
      });
      elements.responseBody.appendChild(row);
    });
  }

  async function request(path) {
    const baseUrl = config.url.replace(/\/+$/, "");
    const response = await fetch(baseUrl + path, {
      method: "GET",
      headers: { Authorization: "Bearer " + config.token }
    });
    const text = await response.text();
    let data;
    try {
      data = text ? JSON.parse(text) : null;
    } catch (error) {
      data = text;
    }
    return { status: response.status, data: data };
  }

  function saveConfig() {
    try {
      localStorage.setItem("pc-gaming-api-config", JSON.stringify(config));
    } catch (error) {
      console.error("No se pudo guardar la configuración en este navegador.", error);
    }
  }

  async function runQuery(path) {
    elements.responseMeta.textContent = "Consultando GET " + path + "...";
    showMessage("Esperando respuesta de la API...");
    try {
      const result = await request(path);
      elements.responseMeta.textContent = "GET " + path + " — HTTP " + result.status;
      if (result.status >= 200 && result.status < 300) {
        renderRows(result.data);
        return true;
      }
      renderRows(Array.isArray(result.data) ? result.data : [result.data]);
      return false;
    } catch (error) {
      elements.responseMeta.textContent = "Error al consultar " + path;
      showMessage("No se pudo conectar. Verifica la URL, el token y la configuración CORS. " + error.message);
      return false;
    }
  }

  elements.url.value = config.url;
  elements.token.value = config.token;

  elements.form.addEventListener("submit", async function (event) {
    event.preventDefault();
    config = {
      url: elements.url.value.trim().replace(/\/+$/, ""),
      token: elements.token.value.trim()
    };
    if (!config.url || !config.token) {
      connected = false;
      elements.queryButton.disabled = true;
      setStatus("ingresa la URL y el token", "offline");
      return;
    }

    saveConfig();
    connected = false;
    elements.queryButton.disabled = true;
    elements.connectButton.disabled = true;
    setStatus("comprobando...", "checking");
    const success = await runQuery("/productos/");
    connected = success;
    elements.queryButton.disabled = !connected;
    elements.connectButton.disabled = false;
    setStatus(success ? "conectada" : "sin conexión", success ? "online" : "offline");
  });

  elements.queryButton.addEventListener("click", async function () {
    if (!connected) return;
    elements.queryButton.disabled = true;
    await runQuery(elements.endpoint.value);
    elements.queryButton.disabled = !connected;
  });
}());
