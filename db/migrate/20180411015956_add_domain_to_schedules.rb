class AddDomainToSchedules < ActiveRecord::Migration[5.1]
  def change
    add_column :schedules, :domain, :string
  end
end
