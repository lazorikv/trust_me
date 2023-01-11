import { useDispatch, useSelector } from "react-redux";
import { timeConvert } from "../../app/utils";
import Paginate from "./Pagination";
import { useEffect, useState } from "react";
import { searchApartments } from "../../features/apartment/apartmentAction";

const ApartmentResult = (props) => {
  const { loading, error, searchApartment, total } = useSelector(
    (state) => state.apartment
  );
  const [currentPage, setCurrentPage] = useState(1);
  const dispatch = useDispatch();

  let city = props.city;

  const handleCreatedAt = (time) => {
    const { year, month, date } = timeConvert(time);
    return (
      <span>
        {date} {month} {year}
      </span>
    );
  };

  const paginate = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  useEffect(() => {
    window.scrollTo({
      left: 0,
      top: 0,
    });
    dispatch(searchApartments({ city, currentPage }));
  }, [currentPage]);

  return (
    <>
      <div className="result">
        <h1>Results</h1>
      </div>
      {searchApartment.length ? (
        searchApartment.map((item) => (
          <div key={item.id} className="apartment">
            <img src="/apartments/apartment.png" alt="Apartment" />
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
                <span>{item.room_count} кімнати</span>
                <span>.</span>
                <span>{item.area} м2</span>
                <span>{item.floor} поверх</span>
              </div>
              <div className="description">
                <span>{item.description}</span>
              </div>
              <div>
                <span className="published">
                  Опубліковано {handleCreatedAt(item.created_at)}
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
