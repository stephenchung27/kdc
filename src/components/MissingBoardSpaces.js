import GasStationIcon from '../images/gas-station.svg';
import ItalianRestaurant from '../images/italian-restaurant.svg';
import TacoStand from '../images/taco-stand.svg'
import SandwichShop from '../images/sandwich-shop.svg'
import Fair from '../images/fair.svg'
import JuiceBar from '../images/juice-bar.svg'
import CoffeeHouse from '../images/coffee-house.svg'
import NightClub from '../images/night-club.svg'
import FlowerGarden from '../images/flower-garden.svg'
import Ballroom from '../images/ballroom.svg'
import Theatre from '../images/theatre.svg'
import Airport from '../images/airport.svg'
import Home from '../images/home.svg'
import JewleryStore from '../images/jewelry-store.svg'
import ShoppingMall from '../images/shopping-mall.svg'
import { useEffect } from 'react';

const nullBoardSpaceCount = {
  'Gas Station': 3,
  'Italian Restaurant': 1,
  'Taco Stand': 1,
  'Sandwich Shop': 1,
  'Fair': 1,
  'Juice Bar': 1,
  'Coffee House': 1,
  'Nightclub': 1,
  'Flower Garden': 1,
  'Ballroom': 1,
  'Theatre': 1,
  'Airport': 1,
  'Home': 1,
  'Jewelry Store': 1,
  'Shopping Mall': 1,
}

const boardSpaceImages = {
  'Gas Station': GasStationIcon,
  'Italian Restaurant': ItalianRestaurant,
  'Taco Stand': TacoStand,
  'Sandwich Shop': SandwichShop,
  'Fair': Fair,
  'Juice Bar': JuiceBar,
  'Coffee House': CoffeeHouse,
  'Nightclub': NightClub,
  'Flower Garden': FlowerGarden,
  'Ballroom': Ballroom,
  'Theatre': Theatre,
  'Airport': Airport,
  'Home': Home,
  'Jewelry Store': JewleryStore,
  'Shopping Mall': ShoppingMall,
}

function MissingBoardSpaces({
  boardSpaces,
  setValidBoard,
  directionNotSet,
}) {

  useEffect(() => {
    let validBoard = true;
    for (const boardSpaceCount of getBoardSpaceCounts()) {
      const [boardSpaceType, count] = boardSpaceCount;
      if (["Jewelry Store", "Shopping Mall"].includes(boardSpaceType)){
        if (count < 0) {
          validBoard = false;
        }
      } else {
        if (count !== 0) {
          validBoard = false;
        }
      }
    }
    if (directionNotSet) {
      validBoard = false;
    }
    setValidBoard(validBoard);
  }, [boardSpaces]);

  function getBoardSpaceCounts() {
    const currentBoardSpaceCount = Object.assign({}, nullBoardSpaceCount);
    for (const row of boardSpaces) {
      for (const boardSpace of row) {
        if (boardSpace) {
          currentBoardSpaceCount[boardSpace] -= 1;
        }
      }
    }

    const resultBoardSpaceCount = [];

    for (const boardSpace in currentBoardSpaceCount) {
      resultBoardSpaceCount.push([boardSpace, currentBoardSpaceCount[boardSpace]]);
    }
  
    return resultBoardSpaceCount;
  }

  return (
    <ul className="missing-board-spaces">
      {getBoardSpaceCounts().map((boardSpaceCount) => {
        const [boardSpaceType, count] = boardSpaceCount;

        if (["Jewelry Store", "Shopping Mall"].includes(boardSpaceType)){
          return (
            <li className={count > 0 ? "missing" : count < 0 ? "bad" : "good"}>
            <div>
              <img src={boardSpaceImages[boardSpaceType]} alt={boardSpaceType}/>
              {boardSpaceType}
            </div>
            <span>
              {count < 0 ? `${-count} extra` : ""}
            </span>
          </li>
          )
        }
        return (
          <li className={count > 0 ? "missing" : count < 0 ? "bad" : "good"}>
            <div>
              <img src={boardSpaceImages[boardSpaceType]} alt={boardSpaceType}/>
              {boardSpaceType}
            </div>
            <span>
              {count > 0 ? `${count} left` : count < 0 ? `${-count} extra` : ""}
            </span>
          </li>
        )
      })}
    </ul>
  )
}

export default MissingBoardSpaces;