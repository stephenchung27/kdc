import blockedHorizontalRoad from '../images/blocked-horizontal-road.png';

function HorizontalRoad({
  blocked,
  toggleHorizontalRoad
}) {
  return (
    <div className='horizontal-road' onClick={toggleHorizontalRoad}>
      {blocked && <img src={blockedHorizontalRoad} 
                       className="blocked-horizontal-road"
                       alt="Blocked horizontal road" />}
    </div>
  )
}

export default HorizontalRoad;
