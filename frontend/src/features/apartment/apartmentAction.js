import { createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

export const createApartment = createAsyncThunk(
  "apartment/create",
  async ({ floor, room_count, area, cost, address }, { rejectWithValue }) => {
    try {
      const userToken = localStorage.getItem("userToken")
        ? localStorage.getItem("userToken")
        : null;
      const config = {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Credentials": "true",
          "Access-Control-Allow-Origin": "*",
          "x-access-token": userToken,
        },
        withCredentials: false,
      };
      const { data } = await axios.post(
        "apartment",
        { floor, room_count, area, cost, address },
        config
      );
      return data;
    } catch (error) {
      if (error.response && error.response.data.message) {
        return rejectWithValue(error.response.data.message);
      } else {
        return rejectWithValue(error.message);
      }
    }
  }
);

export const getApartment = createAsyncThunk(
  "apartment/fetch",
  async ({ id }, rejectWithValue) => {
    try {
      const userToken = localStorage.getItem("userToken")
        ? localStorage.getItem("userToken")
        : null;
      const config = {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Credentials": "true",
          "Access-Control-Allow-Origin": "*",
          "x-access-token": userToken,
        },
        withCredentials: false,
      };
      const { data } = await axios.get(`apartment/${id}`, config);
      return data;
    } catch (error) {
      if (error.response && error.response.data.message) {
        return rejectWithValue(error.response.data.message);
      } else {
        return rejectWithValue(error.message);
      }
    }
  }
);

export const getAllApartments = createAsyncThunk(
  "apartments/fetch",
  async ({}, rejectWithValue) => {
    try {
      const userToken = localStorage.getItem("userToken")
        ? localStorage.getItem("userToken")
        : null;
      const config = {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Credentials": "true",
          "Access-Control-Allow-Origin": "*",
          "x-access-token": userToken,
        },
        withCredentials: false,
      };
      const { data } = await axios.get(`apartment`, config);
      return data;
    } catch (error) {
      if (error.response && error.response.data.message) {
        return rejectWithValue(error.response.data.message);
      } else {
        return rejectWithValue(error.message);
      }
    }
  }
);
