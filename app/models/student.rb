class Student < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable

  validates :first_name, :presence => true
  validates :last_name, :presence => true
  validates :year, :presence => true

  enum sem: [:fall, :spring]

  def admin
    TRUE
    #has_role?(:admin)
  end
end
