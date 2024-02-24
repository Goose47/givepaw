import axios from 'axios';

export const register = async (
  username: string,
  name: string,
  surname: string,
  patronymic: string,
  email: string,
  password: string,
  city_id: number,
  avatar: Blob
) => {
  const formData = new FormData();
  formData.append('username', username);
  formData.append('name', name);
  formData.append('surname', surname);
  formData.append('patronymic', patronymic);
  formData.append('email', email);
  formData.append('password', password);
  formData.append('city_id', city_id.toString());
  formData.append('avatar', avatar);

  try {
    const response = await axios.post('auth/register', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        withCredentials: true,
      },
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const login = async (login: string, password: string) => {
  try {
    const response = await axios.post('auth/login', { login, password });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
