import React, { useEffect, useRef, useState } from "react";
import usePlacesAutocomplete from "./use-places-autocomplite";
import { useDispatch } from "react-redux";
import { searchApartments } from "../../features/apartment/apartmentAction";
import ApartmentResult from "./ApartmentResult";

export default function PredictionsOnInputChange() {
  const [selectedPrediction, setSelectedPrediction] = useState(null);
  const [searchValue, setSearchValue] = useState("");
  const predictions = usePlacesAutocomplete(searchValue);
  const [openSearch, setOpenSearch] = useState(false);
  const [placeToSearch, setPlaceToSearch] = useState("");
  const catMenu = useRef(null);
  const dispatch = useDispatch();

  const handlePredictionSelection = (e, prediction) => {
    e.preventDefault();
    setOpenSearch(false);
    setSearchValue(prediction?.structured_formatting?.main_text);
    setSelectedPrediction(prediction);
  };

  const submitSelection = () => {
    setPlaceToSearch(selectedPrediction);
  };

  useEffect(() => {
    if (placeToSearch !== null) {
      let currentPage = 1;
      let city = placeToSearch?.structured_formatting?.main_text;
      dispatch(searchApartments({ city, currentPage }));
    }
  }, [placeToSearch]);

  const handleEnter = (e) => {
    setSearchValue(e.target.value);
    setOpenSearch(true);
  };

  const closeOpenMenus = (e) => {
    if (catMenu.current && openSearch && !catMenu.current.contains(e.target)) {
      setOpenSearch(false);
    }
  };

  document.addEventListener("mousedown", closeOpenMenus);

  useEffect(() => {
    if (searchValue === "") {
      setOpenSearch(false);
    }
  }, [searchValue]);

  return (
    <>
      <div className="search">
        <div className="searchMain">
          <input
            name="predictionSearch"
            value={searchValue}
            onChange={(e) => handleEnter(e)}
            placeholder="Enter..."
          />
          {openSearch ? (
            <div ref={catMenu} className="dropDown">
              <ul>
                {predictions?.map((prediction) => (
                  <li key={prediction?.place_id}>
                    <button
                      onClick={(e) => handlePredictionSelection(e, prediction)}
                      onKeyDown={(e) =>
                        handlePredictionSelection(e, prediction)
                      }
                    >
                      {prediction?.structured_formatting?.main_text ||
                        "Not found"}
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          ) : null}
        </div>
        <div className="search-btn">
          <button onClick={submitSelection}>Submit</button>
        </div>
      </div>
      <ApartmentResult city={placeToSearch?.structured_formatting?.main_text} />
    </>
  );
}
