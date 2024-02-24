import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { getPets } from '../../service/data.service';

export const fetchPets = createAsyncThunk('pets/fetchPets', async () => {
  return await getPets();
});

const PetSlice = createSlice({
  name: 'pets',
  initialState: {
    pets: [],
    isLoading: false,
    hasError: false,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchPets.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchPets.fulfilled, (state, action) => {
        state.pets = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchPets.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      });
  },
});

export const selectPets = (state: any) => state.pets.pets;
export const selectLoading = (state: any) => state.pets.isLoading;
export const selectError = (state: any) => state.pets.hasError;

export default PetSlice.reducer;
