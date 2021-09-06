import { useEffect, useRef } from 'react';
import '../css/board-space-menu.css'

function BoardSpaceMenu({
  closeMenu,
  setBoardSpace,
}) {
  const ref = useRef(null);

  useEffect(() => {
    function handleClickOutside(event) {
      event.stopPropagation();
      if (ref.current && !ref.current.contains(event.target)) {
        closeMenu()
      }
    }

    document.addEventListener('mousedown', handleClickOutside);

    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    }
  }, [ref, closeMenu]);

  function setBoardSpaceAndClose(boardSpaceType) {
    setBoardSpace(boardSpaceType);
    closeMenu();
  }

  return (
    <div className='board-space-menu' ref={ref}>
            <button
        className="menu-button empty-block"
        onClick={() => setBoardSpaceAndClose(null)} />
      <button
        className="menu-button ballroom"
        onClick={() => setBoardSpaceAndClose("Ballroom")} />
      <button
        className="menu-button coffee-house"
        onClick={() => setBoardSpaceAndClose("Coffee House")} />
      <button
        className="menu-button fair"
        onClick={() => setBoardSpaceAndClose("Fair")} />
      <button
        className="menu-button flower-garden"
        onClick={() => setBoardSpaceAndClose("Flower Garden")} />
      <button
        className="menu-button gas-station"
        onClick={() => setBoardSpaceAndClose("Gas Station")} />
      <button
        className="menu-button italian-restaurant"
        onClick={() => setBoardSpaceAndClose("Italian Restaurant")} />
      <button
        className="menu-button juice-bar"
        onClick={() => setBoardSpaceAndClose("Juice Bar")} />
      <button
        className="menu-button nightclub"
        onClick={() => setBoardSpaceAndClose("Nightclub")} />
      <button
        className="menu-button sandwich-shop"
        onClick={() => setBoardSpaceAndClose("Sandwich Shop")} />
      <button
        className="menu-button taco-stand"
        onClick={() => setBoardSpaceAndClose("Taco Stand")} />
      <button
        className="menu-button theatre"
        onClick={() => setBoardSpaceAndClose("Theatre")} />
      <button
        className="menu-button airport"
        onClick={() => setBoardSpaceAndClose("Airport")} />
      <button
        className="menu-button shopping-mall"
        onClick={() => setBoardSpaceAndClose("Shopping Mall")} />
      <button
        className="menu-button jewelry-store"
        onClick={() => setBoardSpaceAndClose("Jewelry Store")} />
      <button
        className="menu-button home"
        onClick={() => setBoardSpaceAndClose("Home")} />
    </div>
  );
}

export default BoardSpaceMenu;
