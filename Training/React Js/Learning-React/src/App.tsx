// import { useState } from "react";

// function App() {

//   const [name, setName] = useState("");
//   const [weight, setWeight] = useState("");
//   const [height, setHeight] = useState("");
//   const [result, setResult] = useState(null);

//   const calculateBMI = async () => {

//     const response = await fetch("http://localhost:8080/bmi", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json"
//       },
//       body: JSON.stringify({
//         name: name,
//         weight: Number(weight),
//         height: Number(height)
//       })
//     });

//     const data = await response.json();
//     setResult(data);
//   };

//   return (
//     <div style={{padding:"40px", fontFamily:"Arial"}}>
//       <h1>BMI Calculator</h1>

//       <input
//         placeholder="Name"
//         value={name}
//         onChange={(e) => setName(e.target.value)}
//       />

//       <br/><br/>

//       <input
//         placeholder="Weight (kg)"
//         value={weight}
//         onChange={(e) => setWeight(e.target.value)}
//       />

//       <br/><br/>

//       <input
//         placeholder="Height (m)"
//         value={height}
//         onChange={(e) => setHeight(e.target.value)}
//       />

//       <br/><br/>

//       <button onClick={calculateBMI}>
//         Calculate BMI
//       </button>

//       {result && (
//         <div style={{marginTop:"20px"}}>
//           <h3>Result</h3>
//           <p>Name: {result.name}</p>
//           <p>BMI: {result.bmi}</p>
//           <p>Category: {result.category}</p>
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;


import { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [weight, setWeight] = useState("");
  const [height, setHeight] = useState("");
  const [result, setResult] = useState<null | { name: string; bmi: number; category: string }>(null);
  
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const calculateBMI = async () => {
    // 1. Réinitialiser les messages précédents
    setError(null);
    setResult(null);

    // 2. Validation côté client (très importante)
    if (!name.trim()) {
      setError("Veuillez entrer votre nom");
      return;
    }

    const weightNum = Number(weight);
    const heightNum = Number(height);

    if (!weight || isNaN(weightNum) || weightNum <= 0) {
      setError("Veuillez entrer un poids valide (nombre > 0)");
      return;
    }

    if (!height || isNaN(heightNum) || heightNum <= 0) {
      setError("Veuillez entrer une taille valide (nombre > 0)");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch("http://localhost:8080/bmi", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name.trim(),
          weight: weightNum,
          height: heightNum,
        }),
      });

      // 3. Vérifier si la réponse est correcte (très important !)
      if (!response.ok) {
        if (response.status === 400) {
          throw new Error("Données invalides envoyées au serveur");
        }
        if (response.status === 500) {
          throw new Error("Erreur côté serveur");
        }
        throw new Error(`Erreur ${response.status} - ${response.statusText}`);
      }

      const data = await response.json();

      // 4. Vérification minimale de la structure de la réponse
      if (!data || typeof data.bmi !== "number" || !data.category) {
        throw new Error("Réponse du serveur invalide");
      }

      setResult(data);
    } catch (err) {
      console.error("Erreur lors du calcul BMI:", err);
      setError(
        err instanceof Error 
          ? err.message 
          : "Une erreur inattendue s'est produite"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial", maxWidth: "500px", margin: "0 auto" }}>
      <h1>Calculateur d'IMC</h1>

      <div style={{ display: "flex", flexDirection: "column", gap: "16px" }}>
        <input
          placeholder="Nom"
          value={name}
          onChange={(e) => setName(e.target.value)}
          disabled={loading}
        />

        <input
          type="number"
          step="0.1"
          min="20"
          max="300"
          placeholder="Poids (kg)"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
          disabled={loading}
        />

        <input
          type="number"
          step="0.01"
          min="0.5"
          max="3"
          placeholder="Taille (m)"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
          disabled={loading}
        />

        <button 
          onClick={calculateBMI}
          disabled={loading}
          style={{
            padding: "12px",
            background: loading ? "#ccc" : "#007bff",
            color: "white",
            border: "none",
            borderRadius: "6px",
            cursor: loading ? "not-allowed" : "pointer",
          }}
        >
          {loading ? "Calcul en cours..." : "Calculer l'IMC"}
        </button>
      </div>

      {error && (
        <div style={{
          marginTop: "20px",
          padding: "12px",
          background: "#ffebee",
          color: "#c62828",
          borderRadius: "6px",
          border: "1px solid #ef9a9a"
        }}>
          {error}
        </div>
      )}

      {result && (
        <div style={{
          marginTop: "24px",
          padding: "20px",
          background: "#e8f5e9",
          borderRadius: "8px",
          border: "1px solid #a5d6a7"
        }}>
          <h3>Résultat pour {result.name}</h3>
          <p style={{ fontSize: "1.4em", margin: "12px 0" }}>
            IMC : <strong>{result.bmi.toFixed(1)}</strong>
          </p>
          <p style={{ fontSize: "1.1em" }}>
            Catégorie : <strong>{result.category}</strong>
          </p>
        </div>
      )}
    </div>
  );
}

export default App;