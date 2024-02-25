import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { editSocial, getSocial } from '../../service/data.service';


export const fetchSocial = createAsyncThunk('social/fetchSocial', async () => {
  return await getSocial();
});

export const fetchUpdateSocial = createAsyncThunk('social/fetchUpdateSocial', async (data: any) => {
    return await editSocial(data.telegram, data.vk);
  });

const SocialSlice = createSlice({
  name: 'social',
  initialState: {
    social: {},
    isLoading: false,
    hasError: false,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchSocial.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchSocial.fulfilled, (state, action) => {
        state.social = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchSocial.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      })
      .addCase(fetchUpdateSocial.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchUpdateSocial.fulfilled, (state, action) => {
        state.social = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchUpdateSocial.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      });
  },
});

export const selectSocial = (state: any) => state.social.social;
export const selectLoading = (state: any) => state.social.isLoading;
export const selectError = (state: any) => state.social.hasError;

export default SocialSlice.reducer;
