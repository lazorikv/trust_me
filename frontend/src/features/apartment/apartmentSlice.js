import { createSlice } from "@reduxjs/toolkit";
import {
  createApartment,
  getApartment,
  getAllApartments,
  searchApartments,
  recommendationApartments,
} from "./apartmentAction";

const initialState = {
  loading: false,
  apartments: [],
  createApart: [],
  getApartById: [],
  searchApartment: [],
  recApartment: [],
  total: null,
  error: null,
  success: false,
};

const apartmentSlice = createSlice({
  name: "apartment",
  initialState,
  reducers: {},
  extraReducers: {
    [createApartment.pending]: (state) => {
      state.loading = true;
      state.error = null;
    },
    [createApartment.fulfilled]: (state, { payload }) => {
      state.loading = false;
      state.createApart.push(payload);
    },
    [createApartment.rejected]: (state, { payload }) => {
      state.loading = false;
      state.error = payload;
    },
    // getApartment
    [getApartment.pending]: (state) => {
      state.loading = true;
      state.error = null;
    },
    [getApartment.fulfilled]: (state, { payload }) => {
      state.loading = false;
      state.getApartById = payload;
    },
    [getApartment.rejected]: (state, { payload }) => {
      state.loading = false;
      state.error = payload;
    },
    // get all apartments
    [getAllApartments.pending]: (state) => {
      state.loading = true;
      state.error = null;
    },
    [getAllApartments.fulfilled]: (state, { payload }) => {
      state.loading = false;
      state.apartments.push(payload);
    },
    [getAllApartments.rejected]: (state, { payload }) => {
      state.loading = false;
      state.error = payload;
    },
    // search
    [searchApartments.pending]: (state) => {
      state.loading = true;
      state.error = null;
    },
    [searchApartments.fulfilled]: (state, { payload }) => {
      state.loading = false;
      state.searchApartment = payload.apartments;
      state.total = payload.total;
    },
    [searchApartments.rejected]: (state, { payload }) => {
      state.loading = false;
      state.error = payload;
    },
    //recommendations
    [recommendationApartments.pending]: (state) => {
      state.loading = true;
      state.error = null;
    },
    [recommendationApartments.fulfilled]: (state, { payload }) => {
      state.loading = false;
      state.recApartment = payload;
    },
    [recommendationApartments.rejected]: (state, { payload }) => {
      state.loading = false;
      state.error = payload;
    },
  },
});

export default apartmentSlice.reducer;
