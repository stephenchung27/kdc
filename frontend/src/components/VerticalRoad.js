import blockedVerticalRoad from '../images/blocked-vertical-road.png';

function VerticalRoad ({
  blocked,
  toggleVerticalRoad
}) {
  return (
    <div className="vertical-road" onClick={toggleVerticalRoad}>
            {blocked && <img src={blockedVerticalRoad} 
                       className="blocked-vertical-road"
                       alt="Blocked vertical road" />}
    </div>
  )
}

export default VerticalRoad;
