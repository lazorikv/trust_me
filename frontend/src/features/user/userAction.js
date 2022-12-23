import {createAsyncThunk} from "@reduxjs/toolkit";
import axios from "axios";

export const registerUser = createAsyncThunk(
    // action type string
    'user/register',
    // callback function
    async ({ first_name, last_name, phone_number, email, password, role }, { rejectWithValue }) => {
    try {
    // configure header's Content-Type as JSON
    const config = {
    headers: {
    'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': 'true',
        "Access-Control-Allow-Origin": "*"
    },
        withCredentials: false,
    }
    // make request to backend
    await axios.post(
        'auth/signup',
        { first_name, last_name, phone_number, email, password, role },
        config
    )
    } catch (error) {
        // return custom error message from API if any
        if (error.response && error.response.data.message) {
            return rejectWithValue(error.response.data.message)
    } else {
        return rejectWithValue(error.message)
    }
    }

    }
)

export const userLogin = createAsyncThunk(
  'user/login',
  async ({ email, password, role }, { rejectWithValue }) => {
    try {
      // configure header's Content-Type as JSON
      const config = {
            headers: {
    'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': 'true',
        "Access-Control-Allow-Origin": "*"
    },
        withCredentials: false,

      }
      const { data } = await axios.post(
        'auth/login',
        { email, password, role },
        config
      )
      // store user's token in local storage
      localStorage.setItem('userToken', data.token)
      return data
    } catch (error) {
      // return custom error message from API if any
      if (error.response && error.response.data.message) {
        return rejectWithValue(error.response.data.message)
      } else {
        return rejectWithValue(error.message)
      }
    }
  }
)

export const getUserDetails = createAsyncThunk(
  'user/getUserDetails',
  async (arg, { getState, rejectWithValue }) => {
    try {
      // get user data from store
      const { user } = getState()
      // configure authorization header with user's token
      const config = {
        headers: {
          "x-access-token": `${user.userToken}`,
        },
      }
      const { data } = await axios.get(`auth/profile`, config)
      return data
    } catch (error) {
      if (error.response && error.response.data.message) {
        return rejectWithValue(error.response.data.message)
      } else {
        return rejectWithValue(error.message)
      }
    }
  }
)