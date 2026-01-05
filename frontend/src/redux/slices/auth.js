import { createSlice } from '@reduxjs/toolkit'

export const authSlice = createSlice({
  name: 'auth',
  initialState: {
    email: null,
    name: null
  },
  reducers: {
    setEmail: (state, action) => {
        state.email = action.payload
    },
    clearEmail: (state) => {
      state.email = null
    },
    setName: (state, action) => {
      state.name = action.payload
    },
    clearName: (state) => {
      state.name = null
    }
  },
})

export const { 
  setEmail, 
  clearEmail,
  setName,
  clearName
} = authSlice.actions

export default authSlice.reducer