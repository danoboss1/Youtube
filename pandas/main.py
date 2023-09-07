import pandas as pd

data_frame = pd.read_csv('fifa_data.csv')

# print(data_frame)

# print(data_frame.head())
# print(data_frame.tail(3))

print(data_frame.describe())


max_age_index = data_frame['Age'].idxmax()

max_age_row = data_frame.loc[max_age_index]
print(max_age_row)

print(data_frame.shape)
print(data_frame.columns)

print(data_frame[['Name', 'Jumping']])


print(data_frame['Name'][data_frame.Jumping >= 70].values)

high_jump_players = data_frame['Name'][data_frame.Jumping >= 70].values

counter = 0

for name in high_jump_players:
    counter += 1

print(f'{counter} players from FIFA jump very high!')