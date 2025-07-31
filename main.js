import React, { useState } from "react";
import Form from "@rjsf/core";
import Papa from "papaparse";

const schema = {
  title: "Importar CSV",
  type: "object",
  properties: {main
    arquivo: {
      type: "string",
      title: "Arquivo CSV",
      format: "data-url",
      description: "Selecione o arquivo CSV para importar"
    },
    tabela_destino: {
      type: "string",
      title: "Tabela destino",
      description: "Nome da tabela no banco de dados"
    }
  },
  required: ["arquivo", "tabela_destino"]
};

export default function ImportadorCSV() {
  const [csvPreview, setCsvPreview] = useState(null);

  const onSubmit = ({ formData }) => {
    if (!formData.arquivo) {
      alert("Selecione um arquivo!");
      return;
    }

    // Decode do arquivo base64
    const [meta, data] = formData.arquivo.split(",");
    const csv = atob(data);

    // Parse do CSV com papaparse
    const resultado = Papa.parse(csv, { header: true });
    setCsvPreview(resultado.data);

    // Aqui você pode enviar pro backend/Azure/etc
    // fetch("/api/importar", { method: "POST", body: JSON.stringify({ tabela: formData.tabela_destino, dados: resultado.data }) })
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto" }}>
      <Form schema={schema} onSubmit={onSubmit} />
      {csvPreview && (
        <div>
          <h3>Prévia dos dados:</h3>
          <pre style={{ maxHeight: 200, overflow: "auto", background: "#eee", padding: 10 }}>
            {JSON.stringify(csvPreview, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
