import React, { useState } from "react";
// the hook we will create
import usePlacesAutocomplete from "./use-places-autocomplite";

export default function PredictionsOnInputChange() {
  const [selectedPrediction, setSelectedPrediction] = useState(null);
  const [searchValue, setSearchValue] = useState("");
  const predictions = usePlacesAutocomplete(searchValue);
  const [openSearch, setOpenSearch] = useState(false);
  const [placeToSearch, setPlaceToSearch] = useState(null);

  const handlePredictionSelection = (e, prediction) => {
    e.preventDefault();
    setOpenSearch(false);
    setSearchValue(prediction?.structured_formatting?.main_text);
    setSelectedPrediction(prediction);
  };

  const submitSelection = () => {
    setPlaceToSearch(selectedPrediction);
  };

  const handleEnter = (e) => {
    setSearchValue(e.target.value);
    setOpenSearch(true);
  };

  return (
    <>
      <form>
        <input
          name="predictionSearch"
          value={searchValue}
          onChange={(e) => handleEnter(e)}
        />
        {openSearch ? (
          <ul>
            {predictions?.map((prediction) => (
              <li key={prediction?.place_id}>
                <button
                  onClick={(e) => handlePredictionSelection(e, prediction)}
                  onKeyDown={(e) => handlePredictionSelection(e, prediction)}
                >
                  {prediction?.structured_formatting?.main_text || "Not found"}
                </button>
              </li>
            ))}
          </ul>
        ) : null}
      </form>
      <button onClick={submitSelection}>Submit</button>
      <h3>
        You selected:{" "}
        {placeToSearch?.structured_formatting?.main_text || "None"}
      </h3>
    </>
  );
}
