import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { login as enter, register } from '../../auth/auth.service';
import { editUser, getUser } from '../../service/data.service';

// check if backend fixed response
export const fetchLogin = createAsyncThunk('user/fetchLogin', async (data: any) => {
  return await enter(data.username, data.password);
});

export const fetchRegister = createAsyncThunk('user/fetchRegister', async (data: any) => {
  const res = await register(
    data.username,
    data.name,
    data.phone,
    data.surname,
    data.patronymic,
    data.email,
    data.password,
    data.city,
    data.avatar
  );
  return res;
});

export const fetchUser = createAsyncThunk('user/fetchUser', async () => {
  const res = await getUser();
  return res;
});

export const fetchUpdateUser = createAsyncThunk('user/fetchUpdateUser', async (data: any) => {
    const res = await editUser(data.surname, data.name, data.patronymic, data.username, data.email, data.city_id);
    return res;
  });
  

const UserSlice = createSlice({
  name: 'user',
  initialState: {
    user: {},
    isLoading: false,
    hasError: false,
  },
  reducers: {
    logout: (state) => {
      state.user = {};
      state.isLoading = false;
      state.hasError = false;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchLogin.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchLogin.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchLogin.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      })
      .addCase(fetchRegister.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchRegister.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchRegister.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      })
      .addCase(fetchUser.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      })
      .addCase(fetchUpdateUser.pending, (state, action) => {
        state.isLoading = true;
        state.hasError = false;
      })
      .addCase(fetchUpdateUser.fulfilled, (state, action) => {
        state.user = action.payload;
        state.isLoading = false;
        state.hasError = false;
      })
      .addCase(fetchUpdateUser.rejected, (state, action) => {
        state.hasError = true;
        state.isLoading = false;
      });
  },
});

export const selectUser = (state: { user: { user: any } }) => state.user.user;
export const selectLoading = (state: { user: { isLoading: any } }) => state.user.isLoading;
export const selectError = (state: { user: { hasError: any } }) => state.user.hasError;
export const { logout } = UserSlice.actions;

export default UserSlice.reducer;
