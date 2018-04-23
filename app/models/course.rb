name = 'ls'
result = `which #{name}`

class Course < ApplicationRecord
  has_many :schedules
  attachment :syllabus_file
end
