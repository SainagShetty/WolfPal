class Course < ApplicationRecord
  has_many :schedules
  attachment :syllabus_file
end
