import { useRef, useState } from "react";
import "../../styles/apartments/sorting.css";

const Sorting = (props) => {
  const sorting = props.sorting;
  const [openDrop, setOpenDrop] = useState(false);
  const catMenu = useRef(null);
  const closeOpenMenus = (e) => {
    if (catMenu.current && openDrop && !catMenu.current.contains(e.target)) {
      setOpenDrop(false);
    }
  };

  document.addEventListener("mousedown", closeOpenMenus);

  const handleOpen = () => {
    setOpenDrop(!openDrop);
  };

  const handleClick = (value) => {
    sorting(value);
    handleOpen();
  };
  return (
    <>
      <div ref={catMenu} className="dropDown">
        <p onClick={handleOpen}>{props.sortingType}</p>
        {openDrop ? (
          <ul>
            <li onClick={() => handleClick("asc")}>Спочатку дешевші</li>
            <li onClick={() => handleClick("desc")}>Спочатку дорогі</li>
            <li onClick={() => handleClick("")}>Звичайне сортування</li>
            <li onClick={() => handleClick("newest")}>Спочатку нові</li>
          </ul>
        ) : null}
      </div>
    </>
  );
};

export default Sorting;
