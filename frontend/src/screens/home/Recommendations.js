import "../../styles/home/recommendations.css";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { recommendationApartments } from "../../features/apartment/apartmentAction";
import { useNavigate } from "react-router-dom";
import { declOfNum } from "../../app/utils";

const Recommendations = () => {
  const { loading, error, recApartment } = useSelector(
    (state) => state.apartment
  );
  const dispatch = useDispatch();
  const navigator = useNavigate();

  useEffect(() => {
    dispatch(recommendationApartments({}));
  }, [dispatch]);

  const openApartment = (apartment_id) => {
    navigator(`/apartments/${apartment_id}`);
  };

  return (
    <>
      <div className="recommend">
        <h1>Recommendations</h1>
        <div className="Items">
          {recApartment.length
            ? recApartment.map((item) => (
                <div
                  key={item.id}
                  onClick={() => openApartment(item.id)}
                  className="apartmentItem"
                >
                  <img
                    src={item.photo[0] ? item.photo[0].url : null}
                    alt="ApartmentPhoto"
                  />
                  <div className="itemData">
                    <span>{item.cost} UAH</span>
                    <span>
                      {item.address.street}, {item.address.house_number} кв.
                      {item.address.apartment_number}
                    </span>
                    <span>
                      {item.address.district}, {item.address.city}
                    </span>
                    <div className="area">
                      <span>
                        {item.room_count}{" "}
                        {declOfNum(item.room_count, [
                          "кімната",
                          "кімнати",
                          "кімнат",
                        ])}
                      </span>
                      <span>.</span>
                      <span>{item.area} м2</span>
                    </div>
                  </div>
                </div>
              ))
            : null}
        </div>
      </div>
    </>
  );
};

export default Recommendations;
