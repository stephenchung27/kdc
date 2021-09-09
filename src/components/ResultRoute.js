import '../css/results.css';

function ResultRoute({ result }) {
  const affectionPoints = Math.round((result.state.food + result.state.drink + result.state.entertainment) / 6);
  return (
    <div className="result-route-wrapper">
      <div className="result-route">
        <span>{result.description}</span>
        <ol>
          {result.route.map((action) => (
            <li>{action}</li>
          ))}
        </ol>
        <div className="route-stats">
          <div>
            <span>Fuel:</span><span>{result.state.fuel}</span>
          </div>
          <div>
            <span>Food:</span><span>{result.state.food}</span>
          </div>
          <div>
            <span>Drink:</span><span>{result.state.drink}</span>
          </div>
          <div>
            <span>Entertainment:</span><span>{result.state.entertainment}</span>
          </div>
          <div>
            <span>Time:</span><span>{result.state.time}</span>
          </div>
          <div>
            <span>Affection Points:</span><span>{affectionPoints}</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ResultRoute;
