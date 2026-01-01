import { configureStore } from '@reduxjs/toolkit'
import authReducer from './slices/auth'

// Ensure store is only created once (singleton pattern)
let storeInstance

const getStore = () => {
  if (!storeInstance) {
    storeInstance = configureStore({
      reducer: {
        auth: authReducer,
      },
      devTools: true,
    })
  }
  return storeInstance
}

// Export the store instance
export const store = getStore()