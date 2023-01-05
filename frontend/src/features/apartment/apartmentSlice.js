import { createSlice } from "@reduxjs/toolkit";
import { createApartment, getApartment } from "./apartmentAction";

const initialState = {
  loading: false,
  apartments: [],
  createApart: [],
  getApartById: [],
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
      state.getApartById.push(payload);
    },
    [getApartment.rejected]: (state, { payload }) => {
      state.loading = false;
      state.error = payload;
    },
  },
});

export default apartmentSlice.reducer;
