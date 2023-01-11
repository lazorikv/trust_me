import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../features/user/userSlice";
import apartmentSlice from "../features/apartment/apartmentSlice";

const store = configureStore({
  reducer: {
    user: userReducer,
    apartment: apartmentSlice,
  },
});
export default store;
