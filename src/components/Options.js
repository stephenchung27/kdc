import { useState } from 'react';
import ResultRoute from './ResultRoute';
import '../css/options.css';

function Options({
  board,
  flipCar
}) {
  const [results, setResults] = useState([]);
  const [calculating, setCalculating] = useState(false);

  async function calculate() {
    setCalculating(true);
    const response = await fetch("./calculate", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(board)
    });
    response.json().then((data) => {
      console.log(data);
      setResults(data);
      setCalculating(false);
    })
  }

  return (
    <div className="options">
      <div>
        <button onClick={flipCar}>FLIP</button>
        <button onClick={calculate} disabled={calculating}>CALCULATE</button>
      </div>
      <div>
        {results.map(result => <ResultRoute result={result} />)}
      </div>
    </div>
  );
}

export default Options;
