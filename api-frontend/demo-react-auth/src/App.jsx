import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <h1>Bienbenido a "SysBib" </h1>
      <h3>Un sistema pensado para la gestion de una bibloteca...</h3>
      <button>Inicia sesion</button>
    </div>
  );
}

export default App;
