function ResultRoute({ result }) {
  return (
    <div>
      <div>{result.description}</div>
      <ol>
        {result.route.map((action) => (
          <li>{action}</li>
        ))}
      </ol>
      <div>
        <div>Fuel: {result.state.fuel}</div>
        <div>Food: {result.state.food}</div>
        <div>Drink: {result.state.drink}</div>
        <div>Entertainment: {result.state.entertainment}</div>
        <div>Time: {result.state.time}</div>
      </div>
    </div>
  );
}

export default ResultRoute;
