import { useSelector } from "react-redux";

const Statistics = () => {
  const { searchApartment } = useSelector((state) => state.apartment);
  const minimax = () => {
    let maxValue = Math.max(...searchApartment.map((o) => o.cost));
    let minValue = Math.min(...searchApartment.map((o) => o.cost));
    return (
      <span>
        Від {minValue} до {maxValue} UAH за квартиру
      </span>
    );
  };
  return (
    <div className="mainScreen">
      <div className="column">
        <span>150 000 + оголошень від реальних орендодавців</span>
      </div>
      <div className="column">{minimax()}</div>
    </div>
  );
};

export default Statistics;
