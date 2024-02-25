import axios from 'axios';

export const register = async (
  username: string,
  name: string,
  phone: string,
  surname: string,
  patronymic: string,
  email: string,
  password: string,
  city: number,
  image: any
) => {
  try {
    const response: any = await axios.post('auth/register', {
      'username': username,
      'name': name,
      'phone': phone,
      'surname': surname,
      'patronymic': patronymic,
      'email': email,
      'password': password,
      'city_id': city.toString(),
      'avatar': image
    }, {
      headers: {
        'Content-Type': "application/json"
      }
    })
    return response.data;
  } catch (error : any) {
    if (error.response.status === 400) {
      alert(error.response.data.detail)
    } else if (error.response.status === 422) {
      alert("Некорректный e-mail адрес")
    }
    return null;
  }
};

export const login = async (username: string, password: string) => {
  try {
    const response = await axios.post('auth/login', { username, password });
    return response.data;
  } catch (error) {
    alert("Некорректный логин или пароль");
    return null;
  }
};
