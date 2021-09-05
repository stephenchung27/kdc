import { useEffect, useState } from 'react';
import BoardSpaceMenu from './BoardSpaceMenu';
import '../css/board-space.css';

const boardSpaceTypeClassNameMapping = {
  'Gas Station': ' gas-station',
  'Italian Restaurant': ' italian-restaurant',
  'Taco Stand': ' taco-stand',
  'Sandwich Shop': ' sandwich-shop',
  'Fair': ' fair',
  'Juice Bar': ' juice-bar',
  'Coffee House': ' coffee-house',
  'Nightclub': ' nightclub',
  'Flower Garden': ' flower-garden',
  'Ballroom': ' ballroom',
  'Theatre': ' theatre',
  'Airport': ' airport',
  'Jewelry Store': ' jewelry-store',
  'Shopping Mall': ' shopping-mall',
  'Home': ' home',
}

Object.freeze(boardSpaceTypeClassNameMapping);

function BoardSpace ({ boardSpaceType, setBoardSpace }) {
  const [open, setOpen] = useState(false);
  const [boardSpaceClassName, setBoardSpaceClassName] = useState('');

  useEffect(() => {
    console.log(boardSpaceType);
    if (boardSpaceType === null) {
      setBoardSpaceClassName('');
    } else {
      setBoardSpaceClassName(boardSpaceTypeClassNameMapping[boardSpaceType]);
    }
  }, [boardSpaceType])

  return (
    <div className='board-space'>
      <div className={`board-space-icon${boardSpaceClassName}`} onClick={() => setOpen(true)}>
      </div>
      {open && <BoardSpaceMenu 
        closeMenu={() => setOpen(false)}
        setBoardSpace={setBoardSpace} />}
    </div>
  )
}

export default BoardSpace;
