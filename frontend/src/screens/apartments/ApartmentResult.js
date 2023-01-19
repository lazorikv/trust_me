import { useDispatch, useSelector } from "react-redux";
import { declOfNum, timeConvert } from "../../app/utils";
import Paginate from "./Pagination";
import { useEffect, useState } from "react";
import {
  getApartment,
  searchApartments,
} from "../../features/apartment/apartmentAction";
import Error from "../../components/Error";
import Sorting from "./Sorting";
import AWS from "aws-sdk";
import { useNavigate } from "react-router-dom";

const ApartmentResult = (props) => {
  const { loading, error, searchApartment, total } = useSelector(
    (state) => state.apartment
  );
  const [currentPage, setCurrentPage] = useState(1);
  const [sortingValue, setSorting] = useState("");
  const [sortingType, setSortingType] = useState("Звичайне сортування");
  const dispatch = useDispatch();
  const navigator = useNavigate();
  let city = props.city;

  const openApartment = (apartment_id) => {
    navigator(`/apartments/${apartment_id}`);
  };

  const paginate = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  const sorting = (value) => {
    switch (value) {
      case "asc":
        setSortingType("Спочатку дешевші");
        break;
      case "desc":
        setSortingType("Спочатку дорогі");
        break;
      case "newest":
        setSortingType("Спочатку нові");
        break;
      default:
        setSortingType("Звичайне сортування");
    }
    setSorting(value);
  };
  useEffect(() => {
    window.scrollTo({
      left: 0,
      top: 0,
    });
    dispatch(searchApartments({ city, currentPage, sortingValue }));
  }, [currentPage, sortingValue]);

  return (
    <>
      <Sorting sorting={sorting} sortingType={sortingType} />
      <div className="result">
        <h1>Results</h1>
      </div>
      {error && <Error>{error}</Error>}
      {searchApartment.length ? (
        searchApartment.map((item) => (
          <div
            key={item.id}
            onClick={() => openApartment(item.id)}
            className="apartment"
          >
            <img
              src={item.photo[0] ? item.photo[0].url : null}
              alt="Apartment"
            />
            <div className="apartmentDetails">
              <span>{item.cost} UAH</span>
              <span className="address">
                {item.address.street}, {item.address.house_number}, кв.
                {item.address.apart_number}
              </span>
              <span className="city">
                {item.address.district}, {item.address.city}
              </span>
              <div className="area">
                <span>
                  {item.room_count}{" "}
                  {declOfNum(item.room_count, ["кімната", "кімнати", "кімнат"])}
                </span>
                <span>.</span>
                <span>{item.area} м2</span>
                <span>{item.floor} поверх</span>
              </div>
              <div className="description">
                <span>{item.description}</span>
              </div>
              <div>
                <span className="published">
                  Опубліковано {timeConvert(item.created_at)}
                </span>
              </div>
            </div>
          </div>
        ))
      ) : (
        <div className="emptyArray">No available apartments in this city(</div>
      )}
      {searchApartment.length ? (
        <Paginate
          totalPosts={total}
          paginate={paginate}
          currentPage={currentPage}
        />
      ) : null}
    </>
  );
};

export default ApartmentResult;
