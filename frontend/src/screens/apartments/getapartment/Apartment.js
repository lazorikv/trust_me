import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { useEffect, useState } from "react";
import "../../../styles/apartments/get_apartment.css";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { getApartment } from "../../../features/apartment/apartmentAction";
import { declOfNum, timeConvert } from "../../../app/utils";

const Apartment = () => {
  const { getApartById } = useSelector((state) => state.apartment);
  const dispatch = useDispatch();
  let { apartment_id } = useParams();
  useEffect(() => {
    dispatch(getApartment({ apartment_id }));
  }, [apartment_id, dispatch]);
  const handleApartmentCount = (count) => {
    let forms = ["квартиру", "квартири", "квартир"];
    let result = declOfNum(count, forms);
    console.log(result);
    return result;
  };
  return (
    <>
      {getApartById.photo ? (
        <div className="images">
          <div className="mainImage">
            <img
              src={getApartById.photo[0] ? getApartById.photo[0].url : null}
              alt="Main"
            />
          </div>
          <Carousel>
            {getApartById
              ? getApartById.photo.slice(1).map((item) => (
                  <div className="Secondary" key={item.url}>
                    <img src={item.url} alt="Secondary" />
                  </div>
                ))
              : null}
          </Carousel>
        </div>
      ) : null}
      <div className="information">
        <div className="apartmentInfo">
          <h2>{getApartById ? getApartById.title : null}</h2>
          <div className="address">
            <span>
              будинок{" "}
              {getApartById.address
                ? getApartById.address.house_number
                : "No data"}
            </span>
            <span>
              вулиця{" "}
              {getApartById.address ? getApartById.address.street : "No data"}
            </span>
            <span>
              район{" "}
              {getApartById.address ? getApartById.address.district : "No data"}
            </span>
            <span>
              місто{" "}
              {getApartById.address ? getApartById.address.city : "No data"}
            </span>
          </div>
          <p>{getApartById.description ? getApartById.description : null}</p>
        </div>
        <div className="landlordInfo">
          <span className="titleName">Орендодавець</span>
          <span>
            {getApartById.landlord ? getApartById.landlord.last_name : null}{" "}
            {getApartById.landlord ? getApartById.landlord.first_name : null}
          </span>
          <div className="phoneNumber">
            {getApartById.landlord
              ? getApartById.landlord.phone_number
              : "No data"}
          </div>
          <span>
            У HOMIEUA з{" "}
            {getApartById.landlord
              ? timeConvert(getApartById.landlord.created_at)
              : null}
          </span>
          <span>
            Здає в оренду{" "}
            {getApartById.landlord
              ? getApartById.landlord.apartment_count
              : null}{" "}
            {getApartById.landlord
              ? handleApartmentCount(getApartById.landlord.apartment_count)
              : null}
          </span>
        </div>
      </div>
    </>
  );
};

export default Apartment;
