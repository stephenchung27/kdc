import carIcon from '../images/car.png';

function CarDirectionOption({
  setDirection,
  direction
}) {
  return (
    <div className="car-direction-options">
      <div className={`direction-option${direction==="Left" ? " selected" : ""}`}
        onClick={() => setDirection("Left")}>
        <img src={carIcon} alt="Left-facing Car"/>
        <span>Left</span>
      </div>
      <div className={`direction-option${direction==="Right" ? " selected" : ""}`}
        onClick={() => setDirection("Right")}>
        <img src={carIcon} alt="Right-facing Car"/>
        <span>Right</span>
      </div>
    </div>
  );
}

export default CarDirectionOption;
