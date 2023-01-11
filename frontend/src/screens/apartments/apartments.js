import "../../styles/apartments/apartments.css";
import PredictionsOnFormSubmission from "./Search";
import ApartmentResult from "./ApartmentResult";
import React from "react";
import Statistics from "./Statistics";
const ApartmentsScreen = () => {
  return (
    <>
      <PredictionsOnFormSubmission />
      <Statistics />
    </>
  );
};

export default ApartmentsScreen;
